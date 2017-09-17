1. 理解意图
2. 如果是USER_LOCATION：
   * 取出里头的词槽（slot）
     1. slot里头有user_department：先匹配department
     2. 没有user_department，但有user_intent，根据user_intent找到对应的department
     3. 两个都没有，兜底
3. 如果是USER_BUY：
   * 取出里头的词槽(slot)
   * 先取出一次词条 user_goods ，筛选出符合条件的商品
     - 再判断是否有其他二级词条
       - user_discount：打折的
       - user_new：最新的
       - user_cheap: 最便宜的