
authorize()

e['switch'] = document.getElementsByClassName('switch')[0]
e['checkbox'] = e.switch.children[0]

var 
appURL = '/Server/Virtual Machines/'
params = {'name': parameters.username}

API.call(appURL+'status', params).then(status => {

    e.checkbox.checked = status

})

function run() {

    var r

    // If the VM is already on
    if (e.checkbox.checked) {

        r = API.auth(appURL+'stop', params)

    // If the VM is already off
    } else {

        r = API.auth(appURL+'start', params)

    }

    r.then(() => alert('State Changed'))

}
