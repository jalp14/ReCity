var options = {
  bottom: '64px', // default: '32px'
  right: 'unset', // default: '32px'
  left: '32px', // default: 'unset'
  time: '0.5s', // default: '0.3s'
  mixColor: '#fff', // default: '#fff'
  backgroundColor: '#fff',  // default: '#fff'
  buttonColorDark: '#100f2c',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  saveInCookies: true, // default: true,
  label: '🌓', // default: ''
  autoMatchOsTheme: true // default: true
}

const darkmode = new Darkmode(options);

window.onload = checkDKMode()

function checkDKMode() {
  if (darkmode.isActivated()) {
    $("#darkswitch").attr('checked', true)
    document.getElementById('recity').style.visibility = true
    document.getElementById('recity-dark').hidden = false
  } else {
    $("#darkswitch").attr('checked', false)
    document.getElementById('recity').hidden = false
    document.getElementById('recity-dark').hidden = true
  }
}

function activateDKMOde() {
  darkmode.toggle()

  if (darkmode.isActivated()) {
    document.getElementById('recity').hidden = true
    document.getElementById('recity-dark').hidden = false
  } else {
    document.getElementById('recity').hidden = false
    document.getElementById('recity-dark').hidden = true
  }

}

