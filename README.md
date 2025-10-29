# 🌸 Iris Flower Classifier

A beautiful, interactive web application for classifying iris flower species based on their physical measurements. Built with pure HTML, CSS, and JavaScript.

## ✨ Features

- 🎨 **Modern UI Design** - Stunning gradient backgrounds with glass-morphism effects
- ✨ **Smooth Animations** - Engaging animations for inputs and results
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices
- 🌺 **Three Iris Species** - Classifies Setosa, Versicolor, and Virginica
- 🚀 **Zero Dependencies** - Pure vanilla JavaScript, no frameworks required
- ⚡ **Instant Classification** - Real-time results with educational information
- 🎯 **Simple Algorithm** - Based on classic decision tree from the Iris dataset

## 🌺 Iris Species

The classifier can identify three species of iris flowers:

| Species | Characteristics | Habitat |
|---------|----------------|---------|
| **Iris Setosa** 🌼 | Short petals, compact form | Arctic and subarctic regions |
| **Iris Versicolor** 🌸 | Medium-sized petals | Wetlands of eastern North America |
| **Iris Virginica** 🌺 | Longest petals, elegant | Southern and eastern United States |

## 📋 Prerequisites

No prerequisites! This is a standalone HTML file that runs in any modern web browser.

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/iris-classifier.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd iris-classifier
   ```

3. **Open the application**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     # Using Python 3
     python -m http.server 8000
     ```

4. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`

## 📖 Usage

1. **Enter Measurements**: Input the four measurements of your iris flower:
   - Sepal Length (cm)
   - Sepal Width (cm)
   - Petal Length (cm)
   - Petal Width (cm)

2. **Classify**: Click the "Classify Iris Species" button

3. **View Results**: See the predicted species with its icon and description

### Example Measurements

Try these sample measurements:

**Iris Setosa:**
- Sepal Length: 5.1 cm
- Sepal Width: 3.5 cm
- Petal Length: 1.4 cm
- Petal Width: 0.2 cm

**Iris Versicolor:**
- Sepal Length: 6.4 cm
- Sepal Width: 3.2 cm
- Petal Length: 4.5 cm
- Petal Width: 1.5 cm

**Iris Virginica:**
- Sepal Length: 6.3 cm
- Sepal Width: 3.3 cm
- Petal Length: 6.0 cm
- Petal Width: 2.5 cm

## 🧠 Classification Algorithm

The classifier uses a simple decision tree algorithm based on the classic Iris dataset:

```
if petal_length < 2.5:
    return "Iris-setosa"
elif petal_width < 1.8:
    return "Iris-versicolor"
else:
    return "Iris-virginica"
```

This rule-based approach achieves good accuracy for typical iris measurements.

## 🎨 Customization

### Changing Colors

Edit the CSS gradient in the `<style>` section:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Modifying the Algorithm

Update the `classifyIris()` function in the `<script>` section:

```javascript
function classifyIris(sepalLength, sepalWidth, petalLength, petalWidth) {
    // Your custom logic here
}
```

## 📊 Dataset Information

This classifier is based on the famous **Iris Dataset** (Fisher, 1936), one of the most well-known datasets in machine learning and statistics.

- **Total Samples**: 150 (50 per species)
- **Features**: 4 (sepal length/width, petal length/width)
- **Classes**: 3 (Setosa, Versicolor, Virginica)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Ideas for Contributions

- [ ] Add machine learning model integration (TensorFlow.js)
- [ ] Include data visualization charts
- [ ] Add more iris species
- [ ] Implement image-based classification
- [ ] Add dark mode toggle
- [ ] Create API endpoint
- [ ] Add unit tests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@bitcrafter21](https://github.com/bitcrafter21)
- LinkedIn: [in/bitcrafter21](https://linkedin.com/in/bitcrafter21)
- Website: [iris-classifier-alpha.vercel.app](https://iris-classifier-alpha.vercel.app/)

## 🙏 Acknowledgments

- Iris Dataset by R.A. Fisher (1936)
- Design inspiration from modern web design trends
- Icon emojis from Unicode Standard

## 📚 References

- Fisher, R. A. (1936). "The use of multiple measurements in taxonomic problems". *Annals of Eugenics*. 7 (2): 179–188.
- UCI Machine Learning Repository - Iris Dataset

## ⭐ Screenshot
<img width="1920" height="1080" alt="Screenshot from 2025-10-29 23-50-49" src="https://github.com/user-attachments/assets/be2e492d-41be-4c1b-9068-21efb05680c1" />
<img width="1920" height="1080" alt="Screenshot from 2025-10-29 23-50-08" src="https://github.com/user-attachments/assets/43e812bd-c667-43b2-ab72-fbaed10a7515" />

Give a ⭐️ if you like this project!

---

**Made with 💜 and HTML/CSS/JavaScript**
