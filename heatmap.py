import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from scipy.stats import gaussian_kde

# Sample data: Random geographical points and their intensity
np.random.seed(42)
lats = np.random.uniform(-60, 80, 200)  # Latitude range
lons = np.random.uniform(-180, 180, 200)  # Longitude range
intensity = np.random.uniform(1, 10, 200)  # Example metric for heatmap

# Create a map
fig = plt.figure(figsize=(14, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()

# Add features: coastlines, borders, etc.
ax.coastlines(resolution='110m')
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, edgecolor='none', facecolor='lightblue')

# Perform KDE for heatmap
xy = np.vstack([lons, lats])
kde = gaussian_kde(xy, weights=intensity)
kde.set_bandwidth(bw_method=0.15)  # Adjust for smoothness

# Generate a grid for evaluation
lon_grid = np.linspace(-180, 180, 500)
lat_grid = np.linspace(-90, 90, 250)
lon_mesh, lat_mesh = np.meshgrid(lon_grid, lat_grid)
grid_coords = np.vstack([lon_mesh.ravel(), lat_mesh.ravel()])
density = kde(grid_coords).reshape(lat_mesh.shape)

# Plot the heatmap
heatmap = ax.pcolormesh(
    lon_mesh, lat_mesh, density,
    transform=ccrs.PlateCarree(),
    cmap='hot', alpha=0.6
)

# Add a color bar
cbar = plt.colorbar(heatmap, orientation='vertical', shrink=0.6, pad=0.05)
cbar.set_label('Heatmap Intensity')

# Finalize plot
plt.title('Advanced Geographical Heatmap')
plt.show()
