
e['options'] = document.getElementById('options')
e['Search'] = document.getElementById('Search')

function getItem(Type, Title, Year) {

    let call = API.call(

        url = '/Servers/Plex/download',

        params = {
            'Type': Type,
            'Title': Title,
            'Year': Year
        }
        
    )

    call.then(t => alert(t))

}

let lterm = ''

setInterval(() => {

	let term = e.Search.value.toLowerCase()

	if (term != lterm) {

        lterm = term

        // Clear all options
        e.options.innerHTML = ''

        //
        fetch(`https://www.omdbapi.com/?apikey=97f79170&s=${term}`).then(r => r.json()).then(t => {

            if (t.Response == 'True') {

                for (x in t.Search) {

                    let i = t.Search[x]

                    i.Year = i.Year.substring(0,4)
                    
                    // Insert element with item details
                    e.options.insertAdjacentHTML('beforeend', `
                        <a 
                            class = "option"
                            onclick = "getItem('${i.Type}', '${i.Title}', ${i.Year})"
                        >${i.Title} (${i.Year})</a>
                    `)
                    
                }

                e.options.insertAdjacentHTML('afterbegin', `<h2>${e.options.children.length} results</h2>`)

            } else {
            
                e.options.innerHTML = `<h1>No Results for</h1> <br> <h1 style="line-break: anywhere;">${term}</h1>`
            
            }

        })

    }

})