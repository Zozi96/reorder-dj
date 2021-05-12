const movies = document.getElementById('movies')
let sortable = Sortable.create(movies, {
    handle: '.handle',
    dragClass: 'dragged',
    chosenClass: 'sortableChosen',
    onChange: () => {
        saveOrderingButton.disabled = false;
    }
})

const saveOrderingButton = document.getElementById('saveOrdering');
const orderingForm = document.getElementById('orderingForm');
const formInput = orderingForm.querySelector('#orderingInput');

const saveOrdering = () => {
    const rows = document.getElementById("movies").querySelectorAll('tr');
    let ids = [];
    for (let row of rows) {
        ids.push(row.dataset.lookup);
    }
    formInput.value = ids.join(',');
    orderingForm.submit();
}

saveOrderingButton.addEventListener('click', saveOrdering);

