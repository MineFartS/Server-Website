
authorize()

e['Top'] = document.getElementById("top")
e['Bottom'] = document.getElementById("bottom")

const data = {
    
    'save': () => {
        API.auth(
            '/Apps/Bookmark/write',
            {
                'Top': e.Top.value,
                'Bottom': e.Bottom.value
            }
        )
    },
    
    'read': () => {
        return API.auth('/Apps/Bookmark/read')
    }

}

data.read().then(t => {
    e.Top.value = t.Top
    e.Bottom.value = t.Bottom
})