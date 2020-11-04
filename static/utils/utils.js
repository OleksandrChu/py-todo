function extractId() {
    const url = window.location.href;
    return parseInt(url
        .substring(url.lastIndexOf('/') - 1)
        .slice(0, -1));
}

function initRequestConfig(method = 'GET', data = {}) {
    return {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }
}