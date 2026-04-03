
e['boxes'] = document.getElementById('boxes')

data = {

    'read': (e) => {

        API.auth('/Apps/ToDo/read', {x:e.id})
            .then(t => e.value = t)

    },

    'save': (e) => {

        API.auth(
            '/Apps/ToDo/save',
            {
                'x': e.id,
                'value': e.value
            }
        )

    }

}
