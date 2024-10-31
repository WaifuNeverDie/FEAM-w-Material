# FEM/FEA with Material 
This Project is build on python 12.3.2
## Features
- **Sales Analysis**: Track monthly and yearly revenue and units sold.
- **Customer Analysis**: Calculate Customer Lifetime Value (CLV), segment customers by revenue.
- **Product Analysis**: Track sales by product, identify top-selling products.
- **Trend Analysis**: Discover monthly and quarterly sales trends.

## Directory Structure
- `src/`: Contains source code.
    - `main.py`: Main script to launch the application.
    - `shape_functions.py`: Core function for calculating shape functions.
    - `ui/`: UI components.
        - `app.py`: Main UI class handling window setup and events.
        - `widgets/`: Custom widgets for displaying information.
    - `utils/plotting.py`: A utility for plotting shape function values.
- `tests/`: Contains unit tests.


### Explanation

This setup is organized to meet professional standards:
- **Modularity**: Separate directories for core components (e.g., models, controllers, services) make it easier to maintain.
- **Scalability**: Each module can grow independently, enabling additional features without structural changes.
- **Testing**: Unit tests ensure core functions and routes work correctly, improving code reliability.
- **Configuration**: `config.py` and `.env` ensure sensitive data is not hardcoded, following best security practices.
- **Documentation**: `README.md` guides users through setup and usage.

## Installation and Usage
### Refer to the initial setup instructions.
1. **Clone the Repository**:
```bash
   git clone https://github.com/yourusername/salesmetrics_dashboard.git
```
2. **Install Dependencies**:
```bash
   pip install -r requirements.txt
```
3. **Set up Environment Variables**
```bash
    DATABASE_URI=your_database_uri
    SECRET_KEY=your_secret_key
```
### Running the Application
```bash
    python src/app.py
```
### Running Tests
To verify functionality:

```bash
    python -m unittest discover -s tests
```