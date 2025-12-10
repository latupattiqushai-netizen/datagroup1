# supermarket.py - Streamlit Business Dashboard dengan Multi-Bahasa

# ============================================
# SUPPRESS WARNINGS SECTION
# ============================================
import warnings
warnings.filterwarnings('ignore')

import os
import sys

# Suppress Streamlit warnings
os.environ['STREAMLIT_SERVER_ENABLE_STATIC_SERVING'] = 'true'
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'

# ============================================
# MAIN IMPORTS
# ============================================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# MULTI-LANGUAGE DICTIONARIES
# ============================================
translations = {
    'en': {
        # UI Elements
        'title': "🛒 Supermarket Business Dashboard",
        'subtitle': "Upload Excel file (.xlsx/.xls). The app will automatically detect date, numeric, and categorical columns. Display 5 analytical charts + KPI area.",
        'upload_label': "📤 Upload Excel File",
        'upload_help': "Upload supermarket sales data file",
        'select_sheet': "📄 Select Sheet",
        'select_sheet_help': "Select sheet containing data",
        'preview': "👁️ Data Preview (first 100 rows)",
        'sidebar_title': "🎛️ Dashboard Controls",
        'data_info': "**Dataset Info:**",
        'rows': "Rows",
        'columns': "Columns",
        'numeric': "Numeric",
        'categorical': "Categorical",
        'date': "Date",
        
        # Chart Controls
        'time_series': "📈 Time Series",
        'select_date': "Date Column",
        'select_value': "Numeric Value",
        'top_categories': "🏆 Top Categories",
        'category_column': "Category Column",
        'value_for_category': "Value for Category",
        'top_n_items': "Number of Top N",
        'distribution': "📊 Distribution",
        'column_for_histogram': "Column for Histogram",
        'correlation': "🔗 Correlation",
        'select_numeric_columns': "Select numeric columns",
        'correlation_warning': "Minimum 2 numeric columns for correlation",
        'category_share': "🍕 Category Share",
        'column_for_pie': "Column for Pie Chart",
        
        # KPI Section
        'kpi_title': "📊 Key Performance Indicators",
        'total_rows': "Total Data Rows",
        'total_numeric': "Total Numeric Value",
        'average_value': "Average Value",
        'unique_values': "Unique Values (Sample)",
        'na': "N/A",
        
        # Charts Titles
        'chart1_title': "1. Time Series Analysis",
        'chart2_title': "2. Top {top_n} Categories",
        'chart3_title': "3. Distribution",
        'chart4_title': "4. Correlation Matrix",
        'chart5_title': "5. Category Share",
        
        # Chart Info Messages
        'ts_info': "⚠️ Select date column and numeric value in sidebar",
        'cat_info': "⚠️ Select category column and numeric value in sidebar",
        'dist_info': "⚠️ Select numeric column for histogram",
        'corr_info': "⚠️ Select minimum 2 numeric columns",
        'share_info': "⚠️ Select category column in sidebar",
        
        # Export Section
        'export_title': "💾 Export Data",
        'download_report': "📥 Download Summary Report",
        'download_csv': "Click to Download CSV",
        'refresh': "🔄 Refresh Dashboard",
        
        # Upload Instructions
        'upload_instructions_title': "👆 **Please upload your supermarket data Excel file**",
        'upload_instructions': """
        **Recommended file format:**
        - Extension: .xlsx or .xls
        - Minimum columns: Date, Product/Category, and Value (numeric)
        - Example columns: `Date`, `Product Name`, `Category`, `Quantity`, `Price`, `Total`
        
        **After upload, dashboard will display:**
        1. Data preview
        2. Key Performance Indicators (KPI)
        3. 5 types of analytical charts
        4. Interactive controls in sidebar
        """,
        'example_structure': "📋 Example Data Structure",
        
        # Success/Error Messages
        'success_upload': "✅ File successfully uploaded: {filename} | Sheet: {sheet}",
        'error_reading': "❌ Error reading Excel file: {error}",
        
        # Footer
        'footer': "🛒 **Supermarket Business Dashboard** v1.0 | Built with Streamlit | Last uploaded: {timestamp}",
        
        # Example Data
        'example_columns': {
            'date': 'Date',
            'product': 'Product',
            'category': 'Category',
            'quantity': 'Quantity',
            'price': 'Price',
            'total': 'Total'
        }
    },
    
    'id': {
        # UI Elements
        'title': "🛒 Dashboard Bisnis Supermarket",
        'subtitle': "Upload file Excel (.xlsx/.xls). Aplikasi akan otomatis mendeteksi kolom tanggal, numerik, dan kategorikal. Menampilkan 5 chart analitik + area KPI.",
        'upload_label': "📤 Upload File Excel",
        'upload_help': "Upload file data penjualan supermarket",
        'select_sheet': "📄 Pilih Sheet",
        'select_sheet_help': "Pilih sheet yang berisi data",
        'preview': "👁️ Preview Data (100 baris pertama)",
        'sidebar_title': "🎛️ Kontrol Dashboard",
        'data_info': "**Info Dataset:**",
        'rows': "Baris",
        'columns': "Kolom",
        'numeric': "Numerik",
        'categorical': "Kategorikal",
        'date': "Tanggal",
        
        # Chart Controls
        'time_series': "📈 Time Series",
        'select_date': "Kolom Tanggal",
        'select_value': "Nilai Numerik",
        'top_categories': "🏆 Top Categories",
        'category_column': "Kolom Kategori",
        'value_for_category': "Nilai untuk Kategori",
        'top_n_items': "Jumlah Top N",
        'distribution': "📊 Distribusi",
        'column_for_histogram': "Kolom untuk Histogram",
        'correlation': "🔗 Korelasi",
        'select_numeric_columns': "Pilih kolom numerik",
        'correlation_warning': "Minimal 2 kolom numerik untuk korelasi",
        'category_share': "🍕 Category Share",
        'column_for_pie': "Kolom untuk Pie Chart",
        
        # KPI Section
        'kpi_title': "📊 Key Performance Indicators",
        'total_rows': "Total Baris Data",
        'total_numeric': "Total Nilai Numerik",
        'average_value': "Rata-rata Nilai",
        'unique_values': "Unique Values (Sample)",
        'na': "Tidak Tersedia",
        
        # Charts Titles
        'chart1_title': "1. Analisis Time Series",
        'chart2_title': "2. Top {top_n} Kategori",
        'chart3_title': "3. Distribusi",
        'chart4_title': "4. Matriks Korelasi",
        'chart5_title': "5. Pembagian Kategori",
        
        # Chart Info Messages
        'ts_info': "⚠️ Pilih kolom tanggal dan nilai numerik di sidebar",
        'cat_info': "⚠️ Pilih kolom kategori dan nilai numerik di sidebar",
        'dist_info': "⚠️ Pilih kolom numerik untuk histogram",
        'corr_info': "⚠️ Pilih minimal 2 kolom numerik",
        'share_info': "⚠️ Pilih kolom kategori di sidebar",
        
        # Export Section
        'export_title': "💾 Export Data",
        'download_report': "📥 Download Laporan Ringkasan",
        'download_csv': "Klik untuk Download CSV",
        'refresh': "🔄 Refresh Dashboard",
        
        # Upload Instructions
        'upload_instructions_title': "👆 **Silakan upload file Excel data supermarket Anda**",
        'upload_instructions': """
        **Format file yang disarankan:**
        - Ekstensi: .xlsx atau .xls
        - Minimal memiliki kolom: Tanggal, Produk/Kategori, dan Nilai (angka)
        - Contoh kolom: `Tanggal`, `Nama Produk`, `Kategori`, `Jumlah`, `Harga`, `Total`
        
        **Setelah upload, dashboard akan menampilkan:**
        1. Preview data
        2. Key Performance Indicators (KPI)
        3. 5 jenis chart analitik
        """,
        'example_structure': "📋 Contoh Struktur Data",
        
        # Success/Error Messages
        'success_upload': "✅ File berhasil diupload: {filename} | Sheet: {sheet}",
        'error_reading': "❌ Error membaca file Excel: {error}",
        
        # Footer
        'footer': "🛒 **Dashboard Bisnis Supermarket** v1.0 | Dibuat dengan Streamlit | Data terakhir diupload: {timestamp}",
        
        # Example Data
        'example_columns': {
            'date': 'Tanggal',
            'product': 'Produk',
            'category': 'Kategori',
            'quantity': 'Jumlah',
            'price': 'Harga',
            'total': 'Total'
        }
    }
}

# ============================================
# LANGUAGE MANAGEMENT FUNCTIONS
# ============================================
def get_translation(key, lang='en'):
    """Get translation for a key in specified language"""
    return translations.get(lang, translations['en']).get(key, key)

def t(key, **kwargs):
    """Translation helper with formatting"""
    lang = st.session_state.get('language', 'en')
    text = get_translation(key, lang)
    if kwargs:
        return text.format(**kwargs)
    return text

# ============================================
# STREAMLIT CONFIG & SESSION STATE
# ============================================
# Initialize session state for language
if 'language' not in st.session_state:
    st.session_state.language = 'en'

st.set_page_config(
    page_title=t('title'),
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# LANGUAGE SWITCHER IN SIDEBAR
# ============================================
def create_language_switcher():
    """Create language switcher in sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌍 Language / Bahasa")
    
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("🇺🇸 English", use_container_width=True, 
                    type="primary" if st.session_state.language == 'en' else "secondary"):
            st.session_state.language = 'en'
            st.rerun()
    
    with col2:
        if st.button("🇮🇩 Indonesia", use_container_width=True,
                    type="primary" if st.session_state.language == 'id' else "secondary"):
            st.session_state.language = 'id'
            st.rerun()
    
    st.sidebar.markdown("---")

# ============================================
# MAIN DASHBOARD UI
# ============================================
def main():
    # Title and subtitle
    st.title(t('title'))
    st.markdown(t('subtitle'))
    
    # Language switcher in sidebar
    create_language_switcher()
    
    # File uploader
    uploaded_file = st.file_uploader(
        t('upload_label'), 
        type=["xlsx", "xls"], 
        help=t('upload_help')
    )
    
    if uploaded_file is not None:
        # Read Excel file
        try:
            xl = pd.read_excel(uploaded_file, sheet_name=None)
        except Exception as e:
            st.error(t('error_reading', error=str(e)))
            st.stop()
        
        # Sheet selection
        sheet_names = list(xl.keys())
        if len(sheet_names) > 1:
            sheet = st.selectbox(
                t('select_sheet'), 
                sheet_names, 
                help=t('select_sheet_help')
            )
        else:
            sheet = sheet_names[0]
        
        df = xl[sheet].copy()
        
        # Show file info
        st.success(t('success_upload', filename=uploaded_file.name, sheet=sheet))
        
        # Data preview
        with st.expander(t('preview')):
            st.dataframe(df.head(100), use_container_width=True)
        
        # Basic cleaning
        df.dropna(axis=1, how="all", inplace=True)
        
        # Detect column types
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        datetime_cols = df.select_dtypes(include=["datetime"]).columns.tolist()
        
        # Auto-detect date columns
        if not datetime_cols:
            for col in df.columns:
                if df[col].dtype == object:
                    try:
                        parsed = pd.to_datetime(df[col], errors="coerce")
                        if parsed.notna().sum() > len(parsed) * 0.3:  # 30% valid dates
                            df[col] = parsed
                            datetime_cols.append(col)
                    except:
                        pass
        
        categorical_cols = [c for c in df.columns if c not in numeric_cols + datetime_cols]
        
        # ============================================
        # SIDEBAR CONTROLS
        # ============================================
        st.sidebar.header(t('sidebar_title'))
        st.sidebar.info(f"""
        {t('data_info')}
        - {t('rows')}: {len(df):,}
        - {t('columns')}: {len(df.columns):,}
        - {t('numeric')}: {len(numeric_cols)}
        - {t('categorical')}: {len(categorical_cols)}
        - {t('date')}: {len(datetime_cols)}
        """)
        
        # Chart 1: Time Series
        st.sidebar.subheader(t('time_series'))
        date_col = st.sidebar.selectbox(t('select_date'), [None] + datetime_cols)
        ts_value_col = st.sidebar.selectbox(t('select_value'), [None] + numeric_cols)
        
        # Chart 2: Top Categories
        st.sidebar.subheader(t('top_categories'))
        cat_col = st.sidebar.selectbox(t('category_column'), [None] + categorical_cols)
        cat_value = st.sidebar.selectbox(t('value_for_category'), [None] + numeric_cols)
        top_n = st.sidebar.slider(t('top_n_items'), 3, 20, 10)
        
        # Chart 3: Distribution
        st.sidebar.subheader(t('distribution'))
        dist_col = st.sidebar.selectbox(t('column_for_histogram'), [None] + numeric_cols)
        
        # Chart 4: Correlation
        st.sidebar.subheader(t('correlation'))
        if len(numeric_cols) > 1:
            default_corr = numeric_cols[:min(6, len(numeric_cols))]
            corr_cols = st.sidebar.multiselect(
                t('select_numeric_columns'), 
                numeric_cols, 
                default=default_corr
            )
        else:
            corr_cols = []
            st.sidebar.warning(t('correlation_warning'))
        
        # Chart 5: Category Share
        st.sidebar.subheader(t('category_share'))
        share_cat = st.sidebar.selectbox(t('column_for_pie'), [None] + categorical_cols)
        
        # ============================================
        # KPI SECTION
        # ============================================
        st.markdown(f"## {t('kpi_title')}")
        
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        with kpi1:
            st.metric(t('total_rows'), f"{len(df):,}")
        
        with kpi2:
            if numeric_cols:
                total_sum = df[numeric_cols].sum().sum()
                st.metric(t('total_numeric'), f"{total_sum:,.0f}")
            else:
                st.metric(t('total_numeric'), t('na'))
        
        with kpi3:
            if numeric_cols:
                avg_val = df[numeric_cols].mean().mean()
                st.metric(t('average_value'), f"{avg_val:,.2f}")
            else:
                st.metric(t('average_value'), t('na'))
        
        with kpi4:
            if categorical_cols:
                unique_vals = sum(df[c].nunique() for c in categorical_cols[:3])
                st.metric(t('unique_values'), f"{unique_vals:,}")
            else:
                st.metric(t('unique_values'), t('na'))
        
        st.markdown("---")
        
        # ============================================
        # CHARTS SECTION
        # ============================================
        # Row 1: Time Series + Top Categories
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(t('chart1_title'))
            if date_col and ts_value_col:
                # Prepare time series data
                ts_data = df[[date_col, ts_value_col]].copy()
                ts_data = ts_data.dropna()
                ts_data[date_col] = pd.to_datetime(ts_data[date_col])
                ts_data = ts_data.groupby(ts_data[date_col].dt.date)[ts_value_col].sum().reset_index()
                
                # Create plot
                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(ts_data[date_col], ts_data[ts_value_col], 
                       marker='o', linewidth=2, markersize=6, color='#2E86AB')
                ax.set_title(f"Trend {ts_value_col} over Time", fontsize=16, fontweight='bold')
                ax.set_xlabel(date_col, fontsize=12)
                ax.set_ylabel(ts_value_col, fontsize=12)
                ax.grid(True, alpha=0.3)
                ax.fill_between(ts_data[date_col], ts_data[ts_value_col], alpha=0.2, color='#2E86AB')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig)
                
                # Show summary stats
                col1a, col1b, col1c = st.columns(3)
                with col1a:
                    st.metric("Max", f"{ts_data[ts_value_col].max():,.0f}")
                with col1b:
                    st.metric("Min", f"{ts_data[ts_value_col].min():,.0f}")
                with col1c:
                    st.metric("Avg", f"{ts_data[ts_value_col].mean():,.0f}")
            else:
                st.info(t('ts_info'))
        
        with col2:
            st.subheader(t('chart2_title', top_n=top_n))
            if cat_col and cat_value:
                # Prepare category data
                cat_data = df.groupby(cat_col)[cat_value].sum().reset_index()
                cat_data = cat_data.sort_values(cat_value, ascending=False).head(top_n)
                
                # Create horizontal bar chart
                fig, ax = plt.subplots(figsize=(10, 6))
                colors = plt.cm.Set3(np.linspace(0, 1, len(cat_data)))
                bars = ax.barh(range(len(cat_data)), cat_data[cat_value], color=colors)
                ax.set_yticks(range(len(cat_data)))
                ax.set_yticklabels(cat_data[cat_col])
                ax.set_xlabel(cat_value)
                ax.set_title(f"Top {top_n} {cat_col} by {cat_value}", fontsize=14)
                ax.invert_yaxis()
                
                # Add value labels
                for i, (bar, val) in enumerate(zip(bars, cat_data[cat_value])):
                    ax.text(val + val*0.01, bar.get_y() + bar.get_height()/2, 
                           f'{val:,.0f}', va='center', fontsize=10)
                
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info(t('cat_info'))
        
        st.markdown("---")
        
        # Row 2: Distribution, Correlation, Share
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.subheader(t('chart3_title'))
            if dist_col:
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.hist(df[dist_col].dropna(), bins=30, edgecolor='black', 
                       alpha=0.7, color='#A23B72')
                ax.set_title(f"Distribution of {dist_col}", fontsize=14)
                ax.set_xlabel(dist_col)
                ax.set_ylabel("Frequency")
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
            else:
                st.info(t('dist_info'))
        
        with col4:
            st.subheader(t('chart4_title'))
            if len(corr_cols) >= 2:
                corr_matrix = df[corr_cols].corr()
                
                fig, ax = plt.subplots(figsize=(10, 8))
                im = ax.imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
                
                # Add labels
                ax.set_xticks(range(len(corr_cols)))
                ax.set_yticks(range(len(corr_cols)))
                ax.set_xticklabels(corr_cols, rotation=45, ha='right')
                ax.set_yticklabels(corr_cols)
                
                # Add colorbar
                cbar = plt.colorbar(im, ax=ax)
                cbar.set_label('Correlation Coefficient')
                
                # Add correlation values
                for i in range(len(corr_cols)):
                    for j in range(len(corr_cols)):
                        text_color = 'white' if abs(corr_matrix.iloc[i, j]) > 0.5 else 'black'
                        ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                               ha='center', va='center', color=text_color,
                               fontsize=9, fontweight='bold')
                
                ax.set_title("Correlation Heatmap", fontsize=14, fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info(t('corr_info'))
        
        with col5:
            st.subheader(t('chart5_title'))
            if share_cat:
                share_data = df[share_cat].value_counts().reset_index()
                share_data.columns = ['Category', 'Count']
                
                # Limit to top categories for readability
                if len(share_data) > 8:
                    share_data = share_data.head(8)
                    st.caption(f"Showing top 8 of {len(df[share_cat].value_counts())} categories")
                
                fig, ax = plt.subplots(figsize=(10, 6))
                
                if len(share_data) <= 8:
                    # Pie chart for few categories
                    colors = plt.cm.Pastel1(range(len(share_data)))
                    wedges, texts, autotexts = ax.pie(
                        share_data['Count'], 
                        labels=share_data['Category'],
                        autopct='%1.1f%%',
                        colors=colors,
                        startangle=90
                    )
                    ax.set_title(f"Share of {share_cat}", fontsize=14)
                    
                    # Improve readability
                    for autotext in autotexts:
                        autotext.set_color('black')
                        autotext.set_fontweight('bold')
                else:
                    # Bar chart for many categories
                    y_pos = range(len(share_data))
                    ax.barh(y_pos, share_data['Count'])
                    ax.set_yticks(y_pos)
                    ax.set_yticklabels(share_data['Category'])
                    ax.set_xlabel('Count')
                    ax.set_title(f"Distribution of {share_cat}", fontsize=14)
                    ax.invert_yaxis()
                
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info(t('share_info'))
        
        # ============================================
        # DATA EXPORT SECTION
        # ============================================
        st.markdown("---")
        st.subheader(t('export_title'))
        
        export_col1, export_col2 = st.columns(2)
        
        with export_col1:
            if st.button(t('download_report'), use_container_width=True):
                # Create summary dataframe
                summary_data = {
                    'Metric': ['Total Rows', 'Total Columns', 'Numeric Columns', 
                              'Categorical Columns', 'Date Columns', 'File Name', 'Sheet Name'],
                    'Value': [len(df), len(df.columns), len(numeric_cols), 
                             len(categorical_cols), len(datetime_cols), 
                             uploaded_file.name, sheet]
                }
                summary_df = pd.DataFrame(summary_data)
                
                # Convert to CSV
                csv = summary_df.to_csv(index=False)
                st.download_button(
                    label=t('download_csv'),
                    data=csv,
                    file_name="dashboard_summary.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        
        with export_col2:
            if st.button(t('refresh'), use_container_width=True):
                st.rerun()
        
        # ============================================
        # FOOTER
        # ============================================
        st.markdown("---")
        st.caption(t('footer', timestamp=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")))

    else:
        # ============================================
        # UPLOAD INSTRUCTIONS
        # ============================================
        st.info(t('upload_instructions_title'))
        st.markdown(t('upload_instructions'))
        
        # Example data structure
        with st.expander(t('example_structure')):
            # Use language-specific column names
            cols = t('example_columns')
            example_data = pd.DataFrame({
                cols['date']: pd.date_range('2024-01-01', periods=5),
                cols['product']: ['Milk', 'Bread', 'Eggs', 'Oil', 'Sugar'] if st.session_state.language == 'en' else ['Susu', 'Roti', 'Telur', 'Minyak', 'Gula'],
                cols['category']: ['Dairy', 'Bakery', 'Dairy', 'Cooking', 'Pantry'] if st.session_state.language == 'en' else ['Dairy', 'Bakery', 'Dairy', 'Cooking', 'Pantry'],
                cols['quantity']: [100, 150, 200, 80, 120],
                cols['price']: [15000, 12000, 25000, 30000, 18000],
                cols['total']: [1500000, 1800000, 5000000, 2400000, 2160000]
            })
            st.dataframe(example_data)

# ============================================
# RUN THE APP
# ============================================
if __name__ == "__main__":
    main()