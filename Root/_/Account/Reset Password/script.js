
function run() {

    // Call API with login details
    let conn = API.call(
        '/login/create',
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
            
            // Click the back button
            e.back.click()

        }

    })

}
