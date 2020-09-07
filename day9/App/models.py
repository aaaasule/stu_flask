# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/9/7 16:23
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from App.ext import db


class ModelBase:

    def save(self):
        db.session.add(self)
        db.session.commit()


class PreviewData(db.Model, ModelBase):
    __tablename__ = "board_preview_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    tenant_id = db.Column(db.Integer, comment="租户id")  # 租户id
    robot_id = db.Column(db.Integer, comment='机器人id')  # 机器人id
    visitor_counts = db.Column(db.Integer, comment='接待人次')  # 访客数（接待人次）
    conversation_rounds = db.Column(db.Integer, comment='对话轮次')  # 对话轮次
    conversation_average = db.Column(db.Float, comment='会话平均轮次')  # 会话平均轮次
    solve_counts = db.Column(db.Integer, comment='解决接待量')  # 解决接待量
    unsolved_rate = db.Column(db.Float, comment='未解决率')  # 未解决率
    knowledge_hit = db.Column(db.Integer, comment='知识命中')  # 知识命中
    no_answer_rate = db.Column(db.Float, comment='无答案率')  # 无答案率
    solve_rate = db.Column(db.Float, comment='解决率')  # 解决率（整个机器人）
    # effective_knowledge_proportion = db.Column(db.Float)  # 知识命中占比（知识命中对话轮次/总对话轮次）
    knowledge_dia_counts = db.Column(db.Integer, comment='知识对话轮次')
    dialogue_counts = db.Column(db.Integer, comment='对话工厂对话轮次')
    recommend_dia_counts = db.Column(db.Integer, comment='推荐对话轮次')

    opt_by = db.Column(db.String(128), comment='操作人')
    create_time = db.Column(db.DateTime, default=db.func.now(), comment='创建时间')
    update_time = db.Column(db.TIMESTAMP, default=db.func.now(), onupdate=db.func.now(),
                            comment="修改时间")  # onudate
    status = db.Column(db.Boolean, default=True, comment='是否有效数据')
    __table_args__ = ({'comment': '数据看板--数据概览'})
