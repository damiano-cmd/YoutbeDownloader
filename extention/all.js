document.body.addEventListener('mousemove', () => {
    browser.storage.local.set({link: window.location.href})
})
/*browser.storage.onChanged.addListener( async (ch, ar) => {
    console.log(ch, ar, window.location.href)
    if (ar == 'local' && ch.look != undefined) {
        browser.storage.local.set({link: window.location.href})
    }
})*/
//top-level-buttons