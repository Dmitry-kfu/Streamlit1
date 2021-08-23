mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = 0.0.0.0:$PORT\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml
