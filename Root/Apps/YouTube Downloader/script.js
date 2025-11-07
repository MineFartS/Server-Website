
e['url'] = document.getElementsByName('url')[0]
e['format'] = document.getElementsByName('format')[0]
e['form'] = document.getElementById('form')
e['submit'] = document.getElementById('submit')

// Regex to extract id from youtube url
let YT_ID_re = /(?:youtube(?:-nocookie)?\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;

function download(event) {

	// prevent page from changing after javascript finishes
	event.preventDefault()

	// Match the given url to the regex
	let match = e.url.value.match(YT_ID_re)

	// Check if a match isn't found
	if (!match) {

		// Set the color of the 'url' field to 'red'
		e.url.style.backgroundColor = 'red'

		// Wait 1 second
		setTimeout(() => {

			// Set the color of the 'url' field back to 'white'
			e.url.style.backgroundColor = 'white'
		
		}, 1000);

		// Stop Execution
		return

	}

	// Get the formatted URL of youtube video
	let url = `https://www.youtube.com/watch?v=${match[1]}`

	// Get the selected format
	let format = e.format.value

	// Remove the 'form' element
	e.form.remove()

	// Insert loading dots
	document.body.insertAdjacentHTML('beforeend', `
		<div class="loader">
			<span></span>
			<span></span>
			<span></span>
			<span></span>
			<span></span>
			<span></span>
		</div>
	`)

	// Get 'loader' element
	e['loader'] = document.getElementsByClassName('loader')[0]

	// Call API
	API.call(
		'/Apps/YouTube Downloader/get',
		{
			'url': url,
			'format': format
		}
	).then(t => {

		// Remove 'loading' element
		e.loader.remove()

		//
		e.back.textContent = 'Back'
		e.back.setAttribute('href', '.')

		// Insert download button
		document.body.insertAdjacentHTML('beforeend', `
			<a
				href = "${API.url + t.url}"
				class = "download"
				download = "${t.name}"
				target = "_blank"
			>Download</a>
		`)

	})

}
