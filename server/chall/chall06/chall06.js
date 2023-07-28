window.onload = function() {
	document.getElementById("cryptform").addEventListener("submit", (e) => {
		e.preventDefault();

		plaintext = document.getElementById("plaintext").value;

		fetch("/challenge", {
			method: "POST",
			body: "plaintext=" + plaintext,
			headers: {
				"Content-type": "application/x-www-form-urlencoded",
			},
		}).then((response) => {
			response.text().then((data) => {
				document.getElementById("ciphertext").textContent = "Ciphertext: \"" + data + "\"";
			});
		});

		return false;
	});
};
