

async function tes() {
    let res = await axios.get('http://localhost:5000/')
    document.getElementById('rich').innerText = res.data.s
}
tes()
document.getElementById('mp3').addEventListener('click', async () => {
    let {link} = await browser.storage.local.get('link')
    axios({method: 'post', url:'http://localhost:5000/mp3', data:{link: link}})
})
document.getElementById('mp4').addEventListener('click', async () => {
    let {link} = await browser.storage.local.get('link')
    axios({method: 'post', url:'http://localhost:5000/mp4', data:{link: link}})
})

/*browser.storage.onChanged.addListener(async (ch, ar) => {
    if (ar == 'local' && ch.link != undefined) {
        let {look} = await browser.storage.local.get('look')
        let {link} = await browser.storage.local.get('link')
        link = String(link).split('&')[0]
        document.getElementById('rich').innerText = link
        axios({method: 'post', url:'http://localhost:5000/'+look, data:{link: link}})
    }
})*/