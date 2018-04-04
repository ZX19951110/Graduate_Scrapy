jobList=('java' 'c++' '大数据' '数据挖掘' 'iOS' '机器学习' 'php' '产品经理' 'python' 'web')

for job in ${jobList[@]}
do
	scrapy crawl lagou -a job=$job
	sleep 15
done
