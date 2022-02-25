chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    var url = tabs[0].url;
});

document.getElementById('url').innerHTML(url)