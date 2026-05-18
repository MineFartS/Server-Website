
// get option element
e['content'] = document.getElementById('content2')


// Fetch 'files/index.json'
fetch('/Apps/Goofy Stuff/Cursed Images/files/index.json').then(r => r.json()).then(items => {

    // Remove invisible items
    items.filter(i => i.Visible)

    // Shuffle items
    items.sort(() => Math.random()-0.5)

    for (let x=0; x<9; x++) {

        // Set the html of the 'content' element to an embed image
        e.content.innerHTML += `<img src="${items[x].URL}?raw=true">`
    
    }

})
