<template>
    <a-table :dataSource="dataSource" :pagination="pagenation" :columns="columns" v-if="mounted"/>
</template>
<script>
let socket
import {WalletMo} from '../type/wallet.js'
export default {
    name:'TranSaction',
    setup() {
      return {
        dataSource: [],
        page_limit:20,
        pagenation:{
            defaultPageSize:5,
            total:0,
            showTotal: total => `Total ${total} data`,
            showSizeChanger:true,
            pageSizeOptions: ['5', '10', '15', '20'],
            onShowSizeChange:(current, pageSize)=>{
                 socket.emit("new_data",{
                    page_index:current,
                    page_limit_count:pageSize
                })
            },
            onChange:(current,pageSize)=> {
                 socket.emit("new_data",{
                    page_index:current,
                    page_limit_count:pageSize
                })
            }
        },
        page_number:1,
        columns:WalletMo,
        isConnected: false,
        mounted:false
      };
    },
    created() {
       
    },
    mounted() {
       socket=this.$socket;
         this.$socket.emit("new_data",{
            page_index:this.page_number,
            page_limit_count:this.page_limit
        })
        this.$socket.on("new_send_data",(resp)=>{
            var data = resp.data;
            var new_data_source=[];
            if(data.length>0)
            {
                for(var i=0;i<data.length;i++)
                {
                    var trans_item=data[i]; 
                    var item={
                        key:(i+1),
                        block:trans_item.block,
                        confirmed:trans_item.confirmed,
                        hash:trans_item.hash,
                        fromaddress:trans_item.ownerAddress,
                        toAddress:trans_item.toAddress
                    }
                    
                    this.new_data_source.push(item)
                    
                }
                this.dataSource=new_data_source.concat(this.dataSource)
                this.$forceUpdate();
            }
        })
        this.$socket.on("send_data",(resp)=>{
             var data=resp.data;
             this.dataSource=[];  
             for(var i=0;i<data.length;i++)
             {
                  var trans_item=data[i]; 
                  var item={
                    key:(i+1),
                    block:trans_item.block,
                    confirmed:trans_item.confirmed,
                    hash:trans_item.hash,
                    fromaddress:trans_item.ownerAddress,
                    toAddress:trans_item.toAddress
                  }
                  
                  this.dataSource.push(item)
                  
             }
            this.pagenation.total=resp.total
            this.mounted=true
            this.$forceUpdate();
    
        })
    },
    

}
</script>