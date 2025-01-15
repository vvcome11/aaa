data <- read_xlsx("G:\\冠心病\\数据\\7.师姐\\所有患者数据-代码.xlsx", col_names = TRUE)
colnames(data)
data <- data[-1,]
# 2. 将从第三列到最后一列的列转换为数值型
data<- data%>%
  mutate(across(3:ncol(data), as.numeric))
# 安装并加载 dplyr 包
library(dplyr)

# 1. 去掉列名中的 "-" 及其后面的部分
colnames(data) <- gsub("-.*", "", colnames(data))  # 删除"-"及其后面的内容

# 2. 查看是否有重复列名
duplicate_cols <- colnames(data)[duplicated(colnames(data))]
duplicate_cols 
# 3. 合并重复的列
# 首先，我们为每对重复的列创建一个新的列，并将其数据进行合并
data_cleaned <- data

# 使用 dplyr 包
library(dplyr)
# 记录合并的列名和新列名
for (col in unique(duplicate_cols)) {
  # 找到所有列名为 col 的列
  cols_to_merge <- which(colnames(data_cleaned) == col)
  
  if (length(cols_to_merge) > 1) {
    # 合并这些列的数据，取和
    data_cleaned[[paste0(col, "+-2")]] <- rowSums(data_cleaned[, cols_to_merge], na.rm = TRUE)
    
    # 删除原来的重复列
    data_cleaned <- data_cleaned[, -cols_to_merge]
  }
}
# 使用 gsub 删除列名中的 '+' 及其后面的内容
colnames(data_cleaned) <- gsub("\\+.*", "", colnames(data_cleaned))

# 查看修改后的列名
colnames(data_cleaned)
# 加载 writexl 包
library(writexl)
setwd("G:\\冠心病\\数据\\7.师姐")
# 将数据保存为 Excel 文件
write_xlsx(data_cleaned, "G:/冠心病/数据/7.师姐/2018-2023的病人数据.xlsx")
