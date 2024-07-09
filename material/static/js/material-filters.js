"use strict";
/* The id's of the filters */
const filtersIds = ["auxiliar-checkbox", "control-checkbox", "tutoria-checkbox"];
/* The checked status of the filters */
const checked = {};
/** Updates the filter status
 *  Overwrites the checked status of the filter
 *  @param filter The filter to update
 */
const updateFilter = (filter) => {
    filter.checked = checked[filter.id] = !checked[filter.id];
};
/** Initializes the filters */
filtersIds.forEach((id) => {
    const element = document.getElementById(id);
    element.addEventListener("click", (event) => {
        const target = event.target;
        updateFilter(target);
    });
    checked[id] = false;
});
