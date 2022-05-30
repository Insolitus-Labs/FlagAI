# Copyright © 2022 BAAI. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
from flagai.auto_model.auto_loader import AutoLoader
import unittest



class AutoLoaderTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.task_name = [
            "seq2seq", "ner", "classification","poetry",
            "title-generation", "semantic-matching", "embedding"
        ]
        self.model_name = [
            "GPT2-base-ch", "T5-base-ch", "T5-base-en","RoBERTa-base-ch",
            "GLM-large-ch","GLM-large-cn", "BERT-base-en"
        ]


    def test_glm_large_en(self):
        for t_name  in self.task_name:
            m_name = 'GLM-large-en'
            
            loader = AutoLoader(task_name=t_name,
                                model_name=m_name,
                                class_num=3,
                                inner_dim=32,
                                only_download_config=True)
            print(
                f"task_name is {t_name}, model_name is {m_name}"
            )
    def test_glm_large_ch(self):
        for t_name  in self.task_name:
            m_name = 'GLM-large-ch'
            
            loader = AutoLoader(task_name=t_name,
                                model_name=m_name,
                                class_num=3,
                                inner_dim=32,
                                only_download_config=True)
            print(
                f"task_name is {t_name}, model_name is {m_name}"
            )
    def test_BERT_base_en(self):
        for t_name  in self.task_name:
            m_name = 'BERT-base-en'
            
            loader = AutoLoader(task_name=t_name,
                                model_name=m_name,
                                class_num=3,
                                inner_dim=32,
                                only_download_config=True)
            print(
                f"task_name is {t_name}, model_name is {m_name}"
            )
    def test_RoBERTa_base_ch(self):
        for t_name  in self.task_name:
            m_name = 'RoBERTa-base-ch'
            
            loader = AutoLoader(task_name=t_name,
                                model_name=m_name,
                                class_num=3,
                                inner_dim=32,
                                only_download_config=True)
            print(
                f"task_name is {t_name}, model_name is {m_name}"
            )

    def test_GPT2_base_ch(self):
        for t_name  in self.task_name:
            m_name = 'GPT2-base-ch'
            
            loader = AutoLoader(task_name=t_name,
                                model_name=m_name,
                                class_num=3,
                                inner_dim=32,
                                only_download_config=True)
            print(
                f"task_name is {t_name}, model_name is {m_name}"
            )
    def test_T5_base_ch(self):
        for t_name  in self.task_name:
            m_name = 'T5-base-ch'
            loader = AutoLoader(task_name=t_name,
                                model_name=m_name,
                                class_num=3,
                                inner_dim=32,
                                only_download_config=True)
            print(
                f"task_name is {t_name}, model_name is {m_name}"
            )
   
def suite():
    suite = unittest.TestSuite()
    suite.addTest(AutoLoaderTestCase('test_GLM-large-ch'))
    suite.addTest(AutoLoaderTestCase('test_GLM-large-en'))
    suite.addTest(AutoLoaderTestCase('test_BERT_base_en'))
    suite.addTest(AutoLoaderTestCase('test_RoBERTa_base_ch'))
    suite.addTest(AutoLoaderTestCase('test_T5_base_ch'))
    suite.addTest(AutoLoaderTestCase('test_GPT2_base_ch'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
