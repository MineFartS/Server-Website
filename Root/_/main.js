// =======================================================
// PATH:

	// Current domain name ('philh.myftp.biz', 'localhost', ...)
	const domain = window.location.href.split('://')[1].split('/')[0]

	// Get protocol ('http', 'https')
	const protocol = window.location.href.split('://')[0]

	// Get path ('/Apps', ...)
	const path = decodeURI(window.location.pathname)

	//
	const href = decodeURIComponent(window.location.href)

	function ParentPathname(p=path) {		
		let path_segs = p.split('/')

		if (p.endsWith('/')) {
			return path_segs.slice(0, -2).join('/') + '/'
		} else {
			return path_segs.slice(0, -1).join('/') + '/'
		}
		
	}

// =======================================================
// ELEMENTS:

	const e = {
		'back': document.getElementById('back'),
		'title': document.getElementById('title')
	}

	// Set title box to the document's title
	e.title.textContent = document.title

	// Check if not under dir '/_/'
	if (!path.startsWith('/_/')) {

		// Set back button text to parent's pathname
		e.back.textContent = ParentPathname(path)

	}

// =======================================================
// API

	const API = {

		'url': `${protocol}://${domain}:8000`,

		'call': (url, params={}) => {

			// Declare the base url for the request
			url = API.url + url

			// Check if any params are given
			if (Object.keys(params).length > 1) {

				// Add all of the params to the url
				for (key in params) {
					url += `&${key}=${params[key]}`
				}

				// Fix the initial '&'
				url = url.replace('&', '?')
				
			}

			// Return a promise object with json formatting
			return fetch(url).then(r => r.json())

		},

		'auth': (url, params={}) => {

			// Add Username to the params
			params['username'] = cookies['username']

			// Add Token to the params
			params['token'] = cookies['token']

			// Return API.call function with updated params
			return API.call(url, params)

		}

	}

// =======================================================
// PARAMETERS:

	const parameters = {}

	// Check if any params are in the url
	if (window.location.href.includes('?')) {

		// Get unformatted param list
		let rparams = window.location.search.substring(1).split('&')

		// Iter through raw params
		for (x in rparams) {

			// Separate the key and value 
			let [key, value] = rparams[x].split('=')

			// Check if value is bool, then format
			if (['true', 'false'].includes(value)) {
				value = (value == 'true')
			}

			// Check if value is Number, then format
			if (!isNaN(Number(value))) {
				value = Number(value)
			}
			
			// Save decoded Value to key in params dict
			parameters[key] = decodeURIComponent(value)

		}

	}

// =======================================================
// COOKIES:

	const cookies = {}

	// Get unformatted cookies list
	var rcookies = document.cookie.split('; ')

	// Iter through raw cookies
	for (x in rcookies) {

		// Separate the key and value
		let [key, value] = rcookies[x].split('=')

		// Check if value is bool, then format
		if (['true', 'false'].includes(value)) {
			value = (value == 'true')
		}

		// Check if value is Number, then format
		if (!isNaN(Number(value))) {
			value = Number(value)
		}
		
		cookies[key] = value
	}

// =======================================================
// AUTHENTICATION:

function authorize() {

	// Repeat every 1 second
	setInterval(() => {

		// Contact server with authentication details and read response
		API.auth('/login/auth').then(t => {

			// If authentication details are invalid
			if (!t.Valid) {

				// Redirect User to the login page
				window.location.href = `/_/Account/Login?dest=${path}`

			}
					
		})

	}, 1000);

}

// =======================================================