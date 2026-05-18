
// get option element
e['content'] = document.getElementById('content')

let name = parameters['name']

let src = `https://philh.myftp.biz/Apps/Goofy%20Stuff/Cursed%20Images/files/${name}`

// Set the html of the 'content' element to an embed image
e.content.innerHTML = `<img src="${src}?raw=true">`

e.title.textContent = 'My Vibe'