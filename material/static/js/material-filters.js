

const filtersIds= ["auxiliar-checkbox", "control-checkbox", "tutoria-checkbox"];
const checked = {};

const updateFilter = (filter) => {
    filter.checked = checked[filter.id] = !checked[filter.id];
}


filtersIds.forEach((id) => {
    const element = document.getElementById(id);
    element.addEventListener("click", (event) => { 
        updateFilter(event.target);
    });
    checked[id] = false;
})