
authorize()

e['Top'] = document.getElementById("top")
e['Bot'] = document.getElementById("bottom")

const data = {
    
    'save': () => {
        API.auth(
            '/Apps/Bookmark/save',
            {
                'Top': e.Top.value,
                'Bot': e.Bot.value
            }
        )
    },
    
    'read': () => {
        API.auth('/Apps/Bookmark/read').then(t => {
            e.Top.value = t.Top
            e.Bot.value = t.Bot
        })
    }

}

data.read()
