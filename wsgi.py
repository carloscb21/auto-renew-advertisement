if __name__ == '__main__':
    from flask_app import app as application
    import os
    application.run(debug=True, use_reloader=False, port=os.environ.get('PORT', 5000))
