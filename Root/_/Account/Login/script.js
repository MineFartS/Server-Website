
function run() {

    // Call API with login details
    let conn = API.call(
        '/login/check',
        {
            'username': e.username.value,
            'password': e.password.value
        }
    )

    // Read Server Response
    conn.then(t => {

        if (t.Alert) {
            alert(t.Alert)
        }

        if (t.Valid) {
            
            // Set 'username' and 'token' cookies
            document.cookie = `username=${e.username.value}; path=/`
            document.cookie = `token=${t.Token}; path=/`

            // Redirect to destination
            window.location.href = dest

        }

    })

}
