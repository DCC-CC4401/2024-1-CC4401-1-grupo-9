var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { getCookie } from "./getCookie.js";
const csrftoken = getCookie('csrftoken');
/* The id's of the filters */
const filtersIds = ["auxiliar-checkbox", "control-checkbox", "tutoria-checkbox"];
const filtersNames = {
    "auxiliar-checkbox": "auxiliar",
    "control-checkbox": "control",
    "tutoria-checkbox": "tutoria"
};
/* The checked status of the filters */
const checked = {};
const yearFilter = document.getElementById("year-filter");
/**  Fetches the materials with the selected filters */
const handleMaterial = (_) => __awaiter(void 0, void 0, void 0, function* () {
    const year = yearFilter === null || yearFilter === void 0 ? void 0 : yearFilter.value;
    try {
        let url = `/api/materials/?year=${year}`;
        filtersIds.forEach((id) => {
            url += `&${filtersNames[id]}=${checked[id]}`;
        });
        const response = yield fetch(url, {
            method: "GET",
            headers: { "X-CSRFToken": csrftoken },
            credentials: "include"
        });
        const data = yield response.json();
        const materialsContainer = document.getElementById("materials-container");
        materialsContainer.innerHTML = "";
        data.forEach((material) => {
            materialsContainer.innerHTML += `
                <div class="material">
                    <a href="${material.material_url}">
                        <img src="${material.img_url}" alt="Material">
                    </a>
                    <div class="name"> ${material.name} </div>
                </div>
            `;
        });
    }
    catch (error) {
        console.error(error);
    }
});
/** Updates the filter status
 *  Overwrites the checked status of the filter
 *  @param filter The filter to update
 */
const updateFilter = (e) => {
    const filter = e.target;
    filter.checked = checked[filter.id] = !checked[filter.id];
};
/** Initializes the filters */
filtersIds.forEach((id) => {
    const element = document.getElementById(id);
    element.addEventListener("click", updateFilter);
    checked[id] = true;
    element.checked = true;
    element.addEventListener("click", handleMaterial);
});
yearFilter.addEventListener("input", handleMaterial);
