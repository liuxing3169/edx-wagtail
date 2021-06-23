# edx-wagtail
Wagtail is an open source content management system built on Django, with a strong community and commercial support. 
It's focused on user experience, and offers precise control for designers and developers.  
This is [Wagtail](https://github.com/wagtail/wagtail/) for Open edX.  
Notice : This code repository is at an early stage, and there are still a lot of unimplemented features. I look forward to your suggestions or direct contributions. 


# Preview
- [HomePage PreView ](docs/preview/homepage-preview.png)
- [Wagtail Sign in](docs/preview/wagtail-admin-login.png)
- [Wagtail admin](docs/preview/wagtail-admin.png)  
↑ Click to preview the picture

# Main Features
- Customize various pictures, texts and links on the homepage
- Dynamically publish course updates to the homepage
- Shared user system with open edx


# Developers
```
git clone https://github.com/liuxing3169/edx-wagtail.git
python3 -m venv edxwt_env
source edxwt_env/bin/activate
cd edx-wagtail
python cms/manage.py runserver
```

# Deploy with open edx
Please refer [INSTALL STEP BY STEP](docs/INSTALL-STEP-BY-STEP.md) for manual installation

# How to Contribute
Contributions are welcome! The fastest way to give feedback is to create an Issue.

# License
The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the [LICENSE](../main/LICENSE) file for details.

