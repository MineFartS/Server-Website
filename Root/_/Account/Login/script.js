
e['newpass'] = document.getElementById('newpassword')

let wrap = new APIwrapper('change')

function run() {

    wrap.run({
        'oldpassword': e.password.value,
        'newpassword': e.newpass.value
    })

}
