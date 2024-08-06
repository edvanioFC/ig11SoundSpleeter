document.getElementById("upload-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const status = document.getElementById("status");
    let audioPlayers = document.getElementById("audio-players");
    let formData = new FormData();
    let audioFile = document.getElementById("audio-file").files[0];

    formData.append("audio", audioFile);

    status.textContent = "Processando...";
    audioPlayers.style.display = "none";

    fetch("http://127.0.0.1:5009/api/process", {
        method: "POST",
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        status.textContent = "Processamento concluído!";
        audioPlayers.style.display = "block";
        
        document.getElementById("voice-player").src = `http://127.0.0.1:5009${data.voice}`;
        document.getElementById("instruments-player").src = `http://127.0.0.1:5009${data.instruments}`;
        
        document.getElementById("voice-download").href = `http://127.0.0.1:5009${data.voice_download}`;
        document.getElementById("instruments-download").href = `http://127.0.0.1:5009${data.instruments_download}`;
    })
    .catch((error) => {
        status.textContent = "Erro no processamento: " + error;
    });
});

document.getElementById("toggle-theme").addEventListener("click", function() {
    document.body.classList.toggle("dark-mode");
    const themeIcon = document.getElementById("theme-icon");
    if (document.body.classList.contains("dark-mode")) {
        themeIcon.src = "assets/day.png";
        themeIcon.alt = "Modo Claro";
    } else {
        themeIcon.src = "assets/moon.png";
        themeIcon.alt = "Modo Escuro";
    }
});


document.getElementById("toggle-language").addEventListener("click", function() {
    const currentLang = document.documentElement.lang;
    const loveElement = document.getElementById("love");
    let anchor = document.createElement("a");
    const languageIcon = document.getElementById("language-icon");
    anchor.href = 'https://github.com/edvanioFC';
    anchor.textContent = 'edvanioFC';

    if (currentLang === "pt-BR") {
        document.documentElement.lang = "en";
        document.getElementById("description").textContent = "Upload a song to separate the vocals from the instruments.";
        document.getElementById("info-text").innerHTML = "This is a simple audio separator that separates the vocals from the instruments in a song.<br>It was created to assist musicians, especially when they want to learn a new song.";
        loveElement.textContent = "Made with ❤️ by ";
        loveElement.appendChild(anchor);
        document.getElementById("upload-btn").textContent = "Process";
        document.getElementById("status").textContent = "Processing completed!";
        document.getElementById("status").style.display = "none";
        document.getElementById("how-title").textContent = "How it works?";
        //this.textContent = "Português";
        languageIcon.src = "assets/pt.png";
        languageIcon.alt = "Switch to Portuguese";
    } else {
        document.documentElement.lang = "pt-BR";
        document.getElementById("description").textContent = "Faça o upload de uma música para separar a voz dos instrumentos.";
        document.getElementById("info-text").innerHTML = "Este é um simples separador de áudio, que separa a voz dos instrumentos de uma música.<br>Foi criado para facilitar o trabalho dos músicos, principalmente quando desejam aprender uma canção nova.";
        loveElement.textContent = "Feito com ❤️ por ";
        loveElement.appendChild(anchor);
        document.getElementById("upload-btn").textContent = "Processar";
        document.getElementById("status").textContent = "Processamento concluído!";
        document.getElementById("status").style.display = "none";
        document.getElementById("how-title").textContent = "Como funciona?";
        languageIcon.src = "assets/en.png";
        languageIcon.alt = "Switch to English";
        //this.textContent = "English";
    }
});
