
e['options'] = document.getElementById('options')
e['search'] = document.getElementById('Search')

// ============================================================================================

function getItem(Type, Title, Year) {

    // Save the current html of the search results
    window.oldHTML = e.options.innerHTML

    //
    e.search.setAttribute('readonly', 'true')

    // Add loading dots
	e.options.innerHTML = `
		<div class="loader">
			<span></span>
			<span></span>
			<span></span>
			<span></span>
			<span></span>
			<span></span>
		</div>
	`

    // Parse the media title
    Title = Title.replace('&', 'and')
    Title = Title.replace(':', '')
    Title = encodeURIComponent(Title)

    // Call the API
    let call = API.call(

        url = '/Server/Plex/download',

        params = {
            'Type': Type,
            'Title': Title,
            'Year': Year
        },

        timeout = 15
        
    )

    // Handle a Failed API response
    call.catch(responseHandler)

    // Handle a Successful API response
    call.then(responseHandler)

}

function responseHandler(t) {
    
    // Show an alert with the response message
    alert(t)

    // Restore the saved search results html
    e.options.innerHTML = oldHTML

    // Allow the search box to be modified
    e.search.removeAttribute('readonly')

}

// ============================================================================================

// Previous Search Term
let lterm = ''

// Loop every 100 ms
setInterval(() => {

	// Current Search Term
    let term = e.search.value.toLowerCase()

    // If Search Term has changed
    if (term != lterm) {

        // Save the Current Term as the Previous Term
        lterm = term

        // Clear all options
        e.options.innerHTML = ''

        // Call 'omdbapi.com'
        fetch(`https://www.omdbapi.com/?apikey=97f79170&s=${term}`).then(r => r.json()).then(t => {

            // If a response is given
            if (t.Response == 'True') {

                // Iter through search results
                for (x in t.Search) {

                    let i = t.Search[x]

                    // Parse the media release year
                    i.Year = i.Year.substring(0,4)
                    
                    // Insert element with item details
                    e.options.insertAdjacentHTML('beforeend', `
                        <img 
                            src     = "${i.Poster}"
                            title   = "${i.Title} (${i.Year})"
                            onclick = "getItem('${i.Type}', '${i.Title}', ${i.Year})"
                            onerror = "this.remove()"
                        >
                    `)
                    
                }

            // If no response is given
            } else {
            
                // Add a 'no results' message
                e.options.innerHTML = `
                    <h1>No Results for</h1>
                    <br>
                    <h1 style="line-break: anywhere;">${term}</h1>
                `

            }

        })

    }

}, 100)

// ============================================================================================