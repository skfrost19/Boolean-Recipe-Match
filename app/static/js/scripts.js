document.addEventListener('DOMContentLoaded', function() {
    const recipeItems = document.querySelectorAll('.recipe-item');
    recipeItems.forEach(item => {
        const infoBtn = item.querySelector('.info-btn');
        infoBtn.addEventListener('click', function() {
            showTooltip(infoBtn);
        });
    });

    document.addEventListener('click', function(event) {
        const tooltips = document.querySelectorAll('.tooltip');
        tooltips.forEach(tooltip => {
            if (!tooltip.contains(event.target) && !tooltip.previousElementSibling.contains(event.target)) {
                tooltip.style.display = 'none';
            }
        });
    });
});

function showTooltip(button) {
    const item = button.parentElement;
    const name = item.getAttribute('data-name');
    const ingredients = JSON.parse(item.getAttribute('data-ingredients'));
    const method = JSON.parse(item.getAttribute('data-method'));
    
    const tooltip = item.querySelector('.tooltip');
    const tooltipContent = tooltip.querySelector('.tooltip-content');
    
    const ingredientsList = ingredients.map(ingredient => `<li>${ingredient}</li>`).join('');
    const methodList = method.map(step => `<li>${step}</li>`).join('');
    
    tooltipContent.innerHTML = `
        <strong>Name:</strong> ${name}<br>
        <strong>Ingredients:</strong><ul>${ingredientsList}</ul>
        <strong>Method:</strong><ul>${methodList}</ul>
    `;
    
    tooltip.style.display = 'block';
}

function closeTooltip(button) {
    const tooltip = button.parentElement;
    tooltip.style.display = 'none';
}

function addIngredient() {
    const container = document.getElementById('ingredients-container');
    
    // Create the operator select element
    const operatorGroup = document.createElement('div');
    operatorGroup.className = 'operator-group';
    
    const select = document.createElement('select');
    select.name = 'operator';
    const optionAnd = document.createElement('option');
    optionAnd.value = 'AND';
    optionAnd.text = 'AND';
    const optionOr = document.createElement('option');
    optionOr.value = 'OR';
    optionOr.text = 'OR';
    
    select.appendChild(optionAnd);
    select.appendChild(optionOr);
    
    operatorGroup.appendChild(select);
    
    // Create the ingredient input element
    const ingredientGroup = document.createElement('div');
    ingredientGroup.className = 'ingredient-group';
    
    const input = document.createElement('input');
    input.type = 'text';
    input.name = 'ingredients';
    input.placeholder = 'Ingredient';
    
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.className = 'remove-btn';
    removeButton.innerHTML = '<i class="fas fa-trash"></i>';
    removeButton.onclick = function() {
        removeIngredient(removeButton);
    };
    
    ingredientGroup.appendChild(input);
    ingredientGroup.appendChild(removeButton);
    
    // Append the operator and ingredient groups to the container
    container.appendChild(operatorGroup);
    container.appendChild(ingredientGroup);
}

function removeIngredient(button) {
    const ingredientGroup = button.parentElement;
    const operatorGroup = ingredientGroup.previousElementSibling;
    
    ingredientGroup.remove();
    if (operatorGroup && operatorGroup.className === 'operator-group') {
        operatorGroup.remove();
    }
}