	
e['content'] = document.getElementById('content')

document.title = 'Test Title'

fetch('MimeTable.json').then(r => r.json()).then(MimeTable => {

    //============================================================================================

    window.media = {}
    
    media['url'] = parameters.file + '?raw=true'

    media['back'] = parameters.file.substring(0, parameters.file.lastIndexOf('/')+1)

    media['name'] = parameters.file.substring(parameters.file.lastIndexOf('/')+1)

    media['ext'] = parameters.file.substring(parameters.file.lastIndexOf('.')+1).toLowerCase()

    media['mime'] = MimeTable[media.ext]

    media['type'] = media.mime.split('/')[0]

    //============================================================================================

    e.back.textContent = media.back
    e.back.setAttribute('href', media.back)

    e.title.textContent = media.name

    //============================================================================================

    e.content.setAttribute('src', media.url)
	e.content.setAttribute('type', media.mime)

    //============================================================================================

	if (media.type == 'audio') {
		e.content.setAttribute('style', 'height: auto')
	}

})
