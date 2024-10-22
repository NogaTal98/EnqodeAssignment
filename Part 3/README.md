# Zero-Trust Score Widget

## Overview

This Vue.js component visually represents the Zero-Trust Score and its metrics using Vuetify for UI. It shows the company’s overall score, risk category, and individual metric scores with descriptions and progress bars.

### Features:
- Displays the overall Zero-Trust Score.
- Shows individual metric scores and descriptions.
- Visualizes scores using progress bars.
- Displays the risk category with a color-coded alert.

## Integration

### Step 1: Install Vuetify
If you don't have Vuetify installed in your Vue project, install it using:

```bash
vue add vuetify
```

### Step 2: Register the Component
In your Vue component, import and register the widget component:

```js
import ZeroTrustWidget from <widget file location>;

export default {
  components: {
    ZeroTrustWidget
  }
};
```

### Step 3: Use the Component in Your Template

```html
<ZeroTrustWidget />
```

### Step 4: Customize the Data
You can modify the data inside the widget by updating the metrics, companyName, and zeroTrustScore fields in the component’s data() function.


