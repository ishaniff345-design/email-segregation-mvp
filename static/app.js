/*
Frontend JavaScript for Email Segregation.
Handles form submission, API calls, and result display.
*/

// Get DOM elements
const emailInput = document.getElementById('emailInput');
const submitBtn = document.getElementById('submitBtn');
const resetBtn = document.getElementById('resetBtn');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');

// Result elements
const categoryBadge = document.getElementById('categoryBadge');
const categoryText = document.getElementById('categoryText');
const confidenceText = document.getElementById('confidenceText');
const confidenceFill = document.getElementById('confidenceFill');
const extractedData = document.getElementById('extractedData');
const jsonViewer = document.getElementById('jsonViewer');

// Event listeners
submitBtn.addEventListener('click', handleSubmit);
resetBtn.addEventListener('click', handleReset);

// Allow Enter key in textarea but allow Ctrl+Enter to submit
emailInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.ctrlKey) {
        handleSubmit();
    }
});

async function handleSubmit() {
    const emailText = emailInput.value.trim();
    
    if (!emailText) {
        showError('Please paste an email to process.');
        return;
    }
    
    try {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Processing...';
        hideError();
        
        // Call API
        const response = await fetch('/extract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email_text: emailText })
        });
        
        if (!response.ok) {
            throw new Error(`API error: ${response.statusText}`);
        }
        
        const result = await response.json();
        displayResults(result);
        
    } catch (error) {
        showError(`Error: ${error.message}`);
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Extract & Classify';
    }
}

function displayResults(result) {
    // Show results section
    resultsSection.style.display = 'block';
    errorSection.style.display = 'none';
    
    // Update category
    const categoryLabel = getCategoryLabel(result.category);
    categoryBadge.textContent = categoryLabel;
    categoryBadge.className = `badge ${result.category}`;
    categoryText.textContent = getCategoryDescription(result.category);
    
    // Update confidence
    const confidencePercent = Math.round(result.confidence * 100);
    confidenceText.textContent = `${confidencePercent}%`;
    confidenceFill.style.width = `${confidencePercent}%`;
    
    // Update extracted data
    displayExtractedData(result.data, result.category);
    
    // Update JSON viewer
    jsonViewer.textContent = JSON.stringify(result, null, 2);
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

function displayExtractedData(data, category) {
    extractedData.innerHTML = '';
    
    if (!data || Object.keys(data).length === 0) {
        extractedData.innerHTML = '<p class="no-data">No data extracted.</p>';
        return;
    }
    
    for (const [key, value] of Object.entries(data)) {
        const fieldLabel = formatFieldName(key);
        const fieldHTML = `
            <div class="data-field">
                <strong>${fieldLabel}</strong>
                <span>${value || 'N/A'}</span>
            </div>
        `;
        extractedData.innerHTML += fieldHTML;
    }
}

function getCategoryLabel(category) {
    const labels = {
        'tonnage': 'Tonnage',
        'cargo_vc': 'Cargo VC',
        'cargo_tc': 'Cargo TC',
        'unknown': 'Unknown'
    };
    return labels[category] || 'Unknown';
}

function getCategoryDescription(category) {
    const descriptions = {
        'tonnage': 'Open vessel availability information.',
        'cargo_vc': 'Voyage charter cargo requirements.',
        'cargo_tc': 'Time charter cargo requirements.',
        'unknown': 'Unable to classify email. Check content and try again.'
    };
    return descriptions[category] || '';
}

function formatFieldName(fieldName) {
    // Convert snake_case to Title Case
    return fieldName
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function showError(message) {
    errorSection.style.display = 'block';
    resultsSection.style.display = 'none';
    document.getElementById('errorMessage').textContent = message;
}

function hideError() {
    errorSection.style.display = 'none';
}

function handleReset() {
    emailInput.value = '';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';
    emailInput.focus();
}