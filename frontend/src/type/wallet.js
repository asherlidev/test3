export  const WalletMo=[
    {
      title:"Block",
      dataIndex:'block',
      key:'block',
      align:'center'
    },
    {
      title:"Confirmed",
      dataIndex:'confirmed',
      key:'confirmed',
      align:'center',
      customRender: (text)=>{
        if(text.value)
        {
          return <span style='color:green'>confirmed</span>
        } else {
          return <span style='color:red'>unconfirmed</span>
        }
      }
    },
    {
      title:"Hash",
      dataIndex:'hash',
      key:'hash',
      align:'center'
   
    },
    {
      title:"Fromaddress",
      dataIndex:'fromaddress',
      key:'fromaddress',
      align:'center'
    },
    {
      title:"ToAddress",
      dataIndex:'toAddress',
      key:'toAddress',
      align:'center'
    }
  ];