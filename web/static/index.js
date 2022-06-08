function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
function deleteExamen(examenId) {
    fetch("/delete-examen", {
      method: "POST",
      body: JSON.stringify({ examenId: examenId }),
    }).then((_res) => {
      window.location.href = "/examenes";
    });
  }
function deleteAgenda(agendaId) {
    fetch("/delete-agenda", {
      method: "POST",
      body: JSON.stringify({ agendaId: agendaId }),
    }).then((_res) => {
      window.location.href = "/agenda";
    });
  }



 