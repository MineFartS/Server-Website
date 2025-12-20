
e['username'] = document.getElementById('username')

function openPage() {

    if (e.username.value == '') {
    
        alert('Username cannot be blank')
    
    } else {

        window.location.href = `${API.url}/Servers/Virtual Machines/connectRDP?name=${e.username.value}`

    }

}