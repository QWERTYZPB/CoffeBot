from aiogram import Router, types, F

from database import req

from settings import lexicon, barista_kb, user_kb

from security import filter


router = Router()



@router.callback_query(F.data.startswith('barista_'), filter.BaristaProtect())
async def handle_barista(cb: types.CallbackQuery):
    await cb.answer()

    action = cb.data.split('_')[-1]
    

    if action == 'profile':
        user = await req.get_user_by_id(cb.from_user.id)
        try:
            await cb.message.edit_text(
                text=lexicon.BARISTA_PROFILE_TEXT.format(
                    name = user.fullname,
                    username = f"[@{user.username}]" if user.username else '',
                ),
                reply_markup=barista_kb.back_to_main()
            )
        except:
            await cb.message.answer(
                text=lexicon.BARISTA_PROFILE_TEXT.format(
                    name = user.fullname,
                    username = f"[@{user.username}]" if user.username else '',
                ),
                reply_markup=barista_kb.back_to_main()
            )
    else:
        try:
            await cb.message.edit_text(lexicon.START_BARISTA_TEXT, reply_markup=barista_kb.main())
        except:
            await cb.message.answer(lexicon.START_BARISTA_TEXT, reply_markup=barista_kb.main())



@router.callback_query(F.data.startswith('addAcup_'), filter.BaristaProtect())
async def handle_confirm_a_cup(cb: types.CallbackQuery):
    await cb.answer()

    action = cb.data.split('_')[-2]
    user_id = int(cb.data.split('_')[-1])
    user = await req.get_user_by_id(user_id)
    try:
        await cb.message.delete()
    except:
        pass
    
    # Add Points
    if action == 'confirm':
        user = await req.update_user(
            user_id=user_id,
            cups=user.cups + 1
        )
        if user:
            await cb.message.answer(
                text=lexicon.SUCCESS_ADD_A_CUP_TEXT.format(
                    cups = user.cups
                ),  reply_markup=user_kb.reply_back_main())
            user_text = lexicon.SUCCESS_ADD_A_CUP_USER_TEXT.format(cups=user.cups, cups_remain=9-user.cups) if user.cups < 10 else\
                    lexicon.ALREADY_10_CUPS_USER_TEXT.format(cups=user.cups)
            await cb.bot.send_message(
                chat_id=user.user_id,
                text=user_text, 
                reply_markup=user_kb.reply_back_main()
            )
            if user.referrer_id and user.is_first_cup:
                referrer = await req.get_user_by_id(user.referrer_id)
                referrer = await req.update_user(
                    user_id=user.referrer_id,
                    cups=referrer.cups+1
                )
                await req.update_user(
                    user_id=user.user_id,
                    is_first_cup=False
                )
                
                if referrer:
                    await cb.bot.send_message(
                        chat_id=user.referrer_id,
                        text=lexicon.REFERRER_SUCCESS_TEXT.format(
                            name = "@"+user.username if user.username else user.fullname,
                            cups=referrer.cups
                        ), reply_markup=user_kb.reply_back_main()
                    )
            return
        
        await cb.message.edit_text(
                text=lexicon.NO_SUCH_USER_TEXT,
                reply_markup=barista_kb.back_to_main()
                )
    
    # Deduct Points
    elif action == 'deduct':
        user = await req.update_user(
            user_id=user_id,
            cups=user.cups - 9
        )
        if user:
            await cb.message.answer(
                text=lexicon.SUCCESS_DEDUCT_A_CUP_TEXT.format(
                    cups = user.cups
                ), reply_markup=user_kb.reply_back_main()
            )
            await cb.bot.send_message(
                chat_id=user.user_id,
                text=lexicon.SUCCESS_DEDUCT_A_CUP_USER_TEXT.format(
                    cups=user.cups
                ), reply_markup=user_kb.reply_back_main()
            )
            return
        
        await cb.message.edit_text(
                text=lexicon.NO_SUCH_USER_TEXT,
                reply_markup=barista_kb.back_to_main()
                )

    # Cancel
    else:
        await cb.message.answer(lexicon.CANCEL_A_CUP_TEXT.format(
            name="@"+user.username if user.username else user.fullname,
            cups=user.cups
        ), reply_markup=user_kb.reply_back_main())