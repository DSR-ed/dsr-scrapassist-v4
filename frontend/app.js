const API = "https://dsr-scrapassist-v4.onrender.com";

document.getElementById("searchForm").addEventListener("submit", async e => {
  e.preventDefault();
  const data = {
    commune: document.getElementById("commune").value,
    rayon: parseInt(document.getElementById("rayon").value),
    effectif: document.getElementById("effectif").value,
    statut: document.getElementById("statut").value,
    telephone: document.getElementById("telephone").checked,
    email: document.getElementById("email").checked
  };
  const res = await fetch(`${API}/search`, { method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify(data) });
  const json = await res.json();
  display(json.results);
});

function display(list) {
  document.getElementById("count").textContent = list.length;
  const cards = document.getElementById("cards");
  cards.innerHTML = "";
  list.forEach(r => {
    const div = document.createElement("div");
    div.className = "card";
    div.innerHTML = `<strong>${r.nom}</strong><br>${r.ville} ${r.cp}`;
    cards.appendChild(div);
  });
  document.getElementById("results").style.display = "block";
  window.results = list;
}

async function exportCSV() {
  const res = await fetch(`${API}/export/csv`, { method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify({results}) });
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a"); a.href = url; a.download = "resultats.csv"; a.click();
}

async function exportPDF() {
  const res = await fetch(`${API}/export/pdf`, { method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify({results}) });
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a"); a.href = url; a.download = "resultats.pdf"; a.click();
}
