c = get_config()
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.ip = '*' # ローカルホスト以外からもアクセス可能にする
c.NotebookApp.open_browser = False # ブラウザが自動で開かないようにする
c.NotebookApp.port = 9999 # サーバーのポートを指定する  security groupも合わせて設定
