const getCookie = (name: string) : string => {
    let cookieValue: string = "";
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/* The id's of the filters */
const filtersIds: string[] = ["auxiliar-checkbox", "control-checkbox", "tutoria-checkbox"];
const filtersNames: { [key: string]: string } = {
    "auxiliar-checkbox": "auxiliar",
    "control-checkbox": "control",
    "tutoria-checkbox": "tutoria"
};

/* The checked status of the filters */
const checked: { [key: string]: boolean } = {};

const yearFilter = document.getElementById("year-filter") as HTMLInputElement;

type Material = {
    name: string,
    img_url: string,
    material_url: string,
};

/**  Fetches the materials with the selected filters */
const handleMaterial = async (_: Event) => {
    const year: string = yearFilter?.value;

    try {
        let url = `/api/materials/?year=${year}`;
        filtersIds.forEach((id: string) => {
            url += `&${filtersNames[id]}=${checked[id]}`;
        });
    
        const response = await fetch(url, {
                method: "GET",
                headers: {"X-CSRFToken": csrftoken},
                credentials: "include"
            });

        const data = await response.json() as Material[]; 

        const materialsContainer = document.getElementById("materials-container") as HTMLDivElement;
        materialsContainer.innerHTML = "";
        data.forEach((material: Material) => {
            materialsContainer.innerHTML += `
                <div class="material">
                    <a href="${material.material_url}">
                        <img src="${material.img_url}" alt="Material">
                    </a>
                    <div class="name"> ${material.name} </div>
                </div>
            `
        });

    } catch (error) {
        console.error(error);
    }
};


/** Updates the filter status
 *  Overwrites the checked status of the filter
 *  @param filter The filter to update
 */
const updateFilter = (e: Event) => {
    const filter = e.target as HTMLInputElement;
    filter.checked = checked[filter.id] = !checked[filter.id];
};

/** Initializes the filters */
filtersIds.forEach((id: string) => {
    const element: HTMLInputElement = document.getElementById(id) as HTMLInputElement;
    element.addEventListener("click", updateFilter);

    checked[id] = true;
    element.checked = true;
    element.addEventListener("click", handleMaterial);
});

yearFilter.addEventListener("input", handleMaterial);




