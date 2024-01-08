document.getElementById('load-text').addEventListener('click', function() {
    fetch('\\wsl.localhost/Ubuntu-20.04/root/QuickInsight/backend/Routes/audios/jpuVc3NvVTiE2.txt')
       .then(response => response.text())
       .then(text => {
         document.getElementById('text-content').innerText = text;
       });
   });