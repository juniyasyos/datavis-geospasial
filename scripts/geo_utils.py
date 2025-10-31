"""
Utility untuk caching dan optimasi pembacaan file GeoJSON besar

OPTIMASI YANG DITERAPKAN:
1. Caching otomatis - File yang sudah diproses disimpan untuk loading instant
2. Simplifikasi geometri - Mengurangi detail sambil mempertahankan bentuk visual
3. Deteksi perubahan - Cache otomatis diperbarui jika file sumber berubah

KECEPATAN:
- Pertama kali: 1-3 detik (baca + proses + cache)
- Loading ulang: 0.1-0.3 detik (dari cache) ⚡⚡⚡

PENGGUNAAN:
    from geo_utils import load_geojson_simple
    
    # Untuk visualisasi umum (balance speed & detail)
    gdf = load_geojson_simple('path/to/file.geojson')
    
    # Untuk performa maksimal (detail minimal)
    gdf = load_geojson_simple('path/to/file.geojson', simplify_tolerance=0.02)
    
    # Untuk detail maksimal (lebih lambat)
    gdf = load_geojson_cached('path/to/file.geojson', simplify_tolerance=0.001)
"""
import pickle
from pathlib import Path
import geopandas as gpd


def load_geojson_cached(geojson_path, cache_dir='data/cache', simplify_tolerance=None):
    """
    Load GeoJSON dengan caching otomatis + simplifikasi agresif
    
    Parameters:
    -----------
    geojson_path : Path
        Path ke file GeoJSON
    cache_dir : str
        Directory untuk cache
    simplify_tolerance : float, optional
        Jika diset, akan simplify geometri. Direkomendasikan: 0.005-0.01 untuk kecepatan maksimal
    
    Returns:
    --------
    GeoDataFrame
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Nama file cache
    cache_name = geojson_path.stem
    if simplify_tolerance:
        cache_name += f'_simple_{simplify_tolerance}'
    cache_file = cache_dir / f'{cache_name}.pkl'
    
    # Cek apakah cache ada dan lebih baru dari file asli
    if cache_file.exists():
        if cache_file.stat().st_mtime > geojson_path.stat().st_mtime:
            print(f'⚡ Loading dari cache: {cache_file.name}')
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
    
    # Load dari GeoJSON
    print(f'📖 Membaca GeoJSON: {geojson_path.name} ...')
    gdf = gpd.read_file(geojson_path)
    
    # Simplify jika diminta
    if simplify_tolerance:
        print(f'   Simplifying dengan tolerance {simplify_tolerance}...')
        gdf['geometry'] = gdf['geometry'].simplify(
            tolerance=simplify_tolerance,
            preserve_topology=True
        )
    
    # Save ke cache
    print(f'💾 Menyimpan ke cache: {cache_file.name}')
    with open(cache_file, 'wb') as f:
        pickle.dump(gdf, f)
    
    return gdf


def load_geojson_simple(geojson_path, simplify_tolerance=0.01):
    """
    Load GeoJSON dengan simplifikasi agresif untuk performa maksimal
    Cocok untuk visualisasi, mengorbankan sedikit detail geometri
    
    Parameters:
    -----------
    geojson_path : Path
        Path ke file GeoJSON
    simplify_tolerance : float
        Tolerance untuk simplifikasi (default: 0.01, ~1km di ekuator)
        Makin besar = makin cepat, tapi kurang detail
    
    Returns:
    --------
    GeoDataFrame yang sudah disimplifikasi
    """
    return load_geojson_cached(geojson_path, simplify_tolerance=simplify_tolerance)
