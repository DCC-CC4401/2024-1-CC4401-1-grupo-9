

/* The id's of the filters */
const filtersIds: string[] = ["auxiliar-checkbox", "control-checkbox", "tutoria-checkbox"];
/* The checked status of the filters */
const checked: { [key: string]: boolean } = {};


/** Updates the filter status
 *  Overwrites the checked status of the filter
 *  @param filter The filter to update
 */
const updateFilter = (filter: HTMLInputElement) => {
    filter.checked = checked[filter.id] = !checked[filter.id];
}


/** Initializes the filters */
filtersIds.forEach((id: string) => {
    const element: HTMLInputElement = document.getElementById(id) as HTMLInputElement;

    element.addEventListener("click", (event: Event) => { 
        const target = event.target as HTMLInputElement;
        updateFilter(target);
    });
    checked[id] = false;
})