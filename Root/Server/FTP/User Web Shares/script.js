
e['username'] = document.getElementById('username')

function openPage() {

    if (e.username.value == '') {
    
        alert('Username cannot be blank')
    
    } else {

        let url = `./${e.username.value}/`

        // Fetch '' in the current directory
        fetch(url).then(r => r.text()).then(t => {

            // Check if 'Auth.ini' exists
            if (t.includes('<title>IIS 10.0 Detailed Error - 404')) {

                alert('Username Not Found')

            } else {

                window.location.href = url

            }
        
        })

    }

}