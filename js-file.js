
function f_dash(){
    const r = fetch('https://api.newrelic.com/graphql',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-api-key': 'NRAK-O5HEY4B7NGN57IFWYFABWK22ZCJ',
                'Access-Control-Allow-Origin': '*',
                
            },
            body: JSON.stringify({
                query: "mutation {\n dashboardCreateSnapshotUrl(guid:\"MzM5MzExMHxWSVp8REFTSEJPQVJEfDU2MTkwMjU\")\n}\n", 
                
            })
        });
        return r;
        console.log(r);
}
const btn = document.querySelector('#btn');
btn.addEventListener('click', () => {
  f_dash();
});