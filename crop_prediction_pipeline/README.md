# Crop Prediction Pipeline

This folder contains a complete end-to-end pipeline for crop prediction using environmental data and machine learning.

## 📁 Folder Structure

```
crop_prediction_pipeline/
├── crop_predictor.ipynb          # ML prediction pipeline notebook
├── data_output/                  # Directory for JSON data files
│   ├── environmental_data_*.json # Complete environmental data
│   ├── soil_data_*.json         # Soil-specific data
│   ├── weather_data_*.json      # Weather-specific data
│   ├── ml_ready_data_*.json     # Formatted data for ML model
│   └── prediction_results_*.json # Final prediction results
└── README.md                    # This file
```

## 🔄 Pipeline Flow

### Step 1: Data Retrieval and Export
1. **Source**: `../data_retriever.ipynb` (modified with JSON export functionality)
2. **Process**: 
   - Fetches soil data from ISRIC SoilGrids API
   - Retrieves weather data from OpenWeather API
   - Combines environmental data
   - Exports to multiple JSON formats
3. **Output**: JSON files in `data_output/` directory

### Step 2: ML Prediction
1. **Source**: `crop_predictor.ipynb`
2. **Process**:
   - Loads latest JSON data files
   - Formats data for ML model consumption
   - Runs crop recommendation model
   - Generates prediction results
3. **Output**: Crop recommendation with environmental context

## 🚀 How to Use

### Prerequisites
- Jupyter Notebook environment
- Required Python packages: `requests`, `json`, `joblib`, `pandas`, `numpy`
- OpenWeather API key (optional, uses sample data if not provided)
- Pre-trained crop recommendation model

### Running the Pipeline

1. **Generate Environmental Data**:
   ```bash
   # Run the data_retriever.ipynb notebook
   # Execute all cells, especially the JSON export cell
   ```

2. **Run Crop Prediction**:
   ```bash
   # Open crop_predictor.ipynb
   # Execute all cells to get crop recommendations
   ```

### Key Features

#### Data Retrieval (`data_retriever.ipynb` - New JSON Export Block)
- ✅ **Environmental Data Export**: Combines soil and weather data
- ✅ **ML-Ready Format**: Structures data for model consumption
- ✅ **Multiple Formats**: Separate and combined JSON files
- ✅ **NPK Mapping**: Maps soil textures to nutrient values
- ✅ **Error Handling**: Graceful fallbacks for missing data

#### ML Prediction Pipeline (`crop_predictor.ipynb`)
- ✅ **Automatic Data Loading**: Finds and loads latest JSON files
- ✅ **Model Integration**: Uses existing crop recommendation model
- ✅ **Feature Preparation**: Formats data for model input
- ✅ **Prediction Results**: Provides crop recommendations
- ✅ **Probability Scores**: Shows confidence levels (if supported)
- ✅ **Environmental Context**: Includes conditions in results
- ✅ **Results Export**: Saves predictions to JSON

## 📊 Data Format

### ML-Ready Data Structure
```json
{
  "N": 80,              // Nitrogen content
  "P": 40,              // Phosphorus content  
  "K": 45,              // Potassium content
  "temperature": 25.5,   // Temperature in Celsius
  "humidity": 65,        // Humidity percentage
  "ph": 7.1,            // Soil pH
  "rainfall": 25.0,      // Rainfall in mm
  "metadata": {
    "timestamp": "2025-08-22 23:22:26",
    "coordinates": {
      "latitude": 20.2575,
      "longitude": 76.7858
    }
  }
}
```

### Prediction Results Structure
```json
{
  "prediction": {
    "recommended_crop": "rice",
    "confidence": "High",
    "probabilities": {
      "rice": 0.85,
      "wheat": 0.10,
      "maize": 0.05
    }
  },
  "environmental_conditions": {
    "location": {...},
    "soil": {...},
    "weather": {...}
  }
}
```

## 🔧 Configuration

### Model Path
The pipeline automatically searches for the crop recommendation model in:
1. `../advisor_lib/crop_recommendation_model.pkl`
2. `../half-baked-stuff/crop_recommendation_model.pkl`

### API Keys
- Set `OPENWEATHER_API_KEY` environment variable for live weather data
- Uses sample data if API key is not provided

## 📈 Expected Model Input
The ML model expects features in this exact order:
1. **N** - Nitrogen content
2. **P** - Phosphorus content
3. **K** - Potassium content
4. **Temperature** - Temperature in Celsius
5. **Humidity** - Humidity percentage
6. **pH** - Soil pH level
7. **Rainfall** - Rainfall in mm

## 🎯 Use Cases

1. **Agricultural Planning**: Determine best crops for specific locations
2. **Environmental Analysis**: Understand soil-weather-crop relationships  
3. **Research**: Analyze environmental factors affecting crop suitability
4. **Decision Support**: Provide data-driven crop recommendations

## 🔄 Integration

This pipeline can be easily integrated with:
- Web applications (via JSON API)
- Agricultural management systems
- Environmental monitoring platforms
- Research analysis workflows

## 📝 Notes

- JSON files are timestamped for version control
- Pipeline handles missing data gracefully
- Results include environmental context for transparency
- Supports both single predictions and batch processing
