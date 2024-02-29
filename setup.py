from setuptools import setup

setup(name='MyShell-OpenVoice',
      version='0.0.0',
      description='Instant voice cloning by MyShell.',
      long_description=open('README.md').read().strip(),
      long_description_content_type='text/markdown',
      keywords=[
            'text-to-speech',
            'tts',
            'voice-clone',
            'zero-shot-tts'
      ],
      url='https://github.com/myshell-ai/OpenVoice',
      project_urls={
        'Documentation': 'https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md',
        'Changes': 'https://github.com/myshell-ai/OpenVoice/releases',
        'Code': 'https://github.com/myshell-ai/OpenVoice',
        'Issue tracker': 'https://github.com/myshell-ai/OpenVoice/issues',
      },
      author='MyShell',
      author_email='ethan@myshell.ai',
      license='Creative Commons Attribution-NonCommercial 4.0 International Public License',
      packages=[
          'openvoice',
          'openvoice.text'
      ],
      python_requires='>=3.9',
      install_requires=[
            'librosa',
            'faster-whisper',
            'pydub',
            'wavmark',
            'numpy',
            'eng_to_ipa',
            'inflect',
            'unidecode',
            'whisper-timestamped',
            'pypinyin',
            'cn2an',
            'jieba',
            'gradio',
            'langid'
      ],
      zip_safe=False
      )
